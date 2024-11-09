<script setup>
import { ref } from 'vue'
import TechnologyTable from './TechnologyTable.vue'
</script>

<template>
    <TechnologyTable :technologies="technologies" @edit-technology="editTechnology"
        @delete-technology="deleteTechnology" />
    <div class="d-flex justify-content-center">
        <button class="btn btn-primary btn-lg mx-auto" data-bs-toggle="modal" data-bs-target="#CreateTechnologyModal">
            Add a new Technology
        </button>
    </div>

    <div class="modal fade" id="CreateTechnologyModal" tabindex="-1" aria-labelledby="exampleModalLabel"
        aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Add a new technology</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>

                <div class="modal-body">
                    <div>
                        <label for="name" class="form-label">Technology Name</label>
                        <input v-model="newTechnology.name" type="text" class="form-control" id="name"
                            placeholder="Name">
                    </div>
                    <div>
                        <label for="type" class="form-label">Technology Type</label>
                        <input v-model="newTechnology.type" type="text" class="form-control" id="type"
                            placeholder="Type">
                    </div>
                    <div>
                        <label for="description" class="form-label">Technology Description</label>
                        <textarea v-model="newTechnology.description" class="form-control" id="description"
                            rows="3"></textarea>
                    </div>
                    <div>
                        <label for="version" class="form-label">Technology Version</label>
                        <input v-model="newTechnology.version" type="number" class="form-control" id="version"
                            placeholder="Version">
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary" @click="createTechnology" data-bs-dismiss="modal">Save
                        changes</button>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
export default {
    components: {
        TechnologyTable,
    },
    data() {
        return {
            title: 'Technologies',
            technologies: [],
            newTechnology: {
                name: '',
                type: '',
                date: '',
                description: ''
            },
        }
    },
    async mounted() {
        const response = await fetch('http://localhost:8000/api/technologies/')
        const data = await response.json()
        this.technologies = data.technologies;
    },
    methods: {
        async deleteTechnology(technology) {
            if (confirm(`Are you sure you want to delete the '${technology.name}' technology?`)) {
                const response = await fetch(`http://localhost:8000/api/technology/${technology.id}`, {
                    method: 'DELETE',
                })
                if (response.ok) {
                    this.technologies = this.technologies.filter(t => t.id !== technology.id)
                    window.dispatchEvent(new Event('DATA_UPDATE'))
                }
            }
        },
        async createTechnology() {
            const response = await fetch('http://localhost:8000/api/technologies/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.newTechnology)
            })
            if (response.ok) {
                const newTechnology = await response.json()
                this.technologies.push(newTechnology)
                window.dispatchEvent(new Event('DATA_UPDATE'))
            }
        },
        async editTechnology(technology) {
            const response = await fetch(`http://localhost:8000/api/technology/${technology.id}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(technology)
            })
            if (response.ok) {
                const updatedTechnology = await response.json()
                const index = this.technologies.findIndex(p => p.id === technology.id)
                this.technologies.splice(index, 1, updatedTechnology)
                window.dispatchEvent(new Event('DATA_UPDATE'))
            }
        }
    }
}
</script>