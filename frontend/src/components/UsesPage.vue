<script setup>
import { ref } from 'vue'
import UsesTable from './UsesTable.vue'
</script>

<template>
    <UsesTable :uses="uses" :projects="projects" :technologies="technologies" @edit-use="editUse"
        @delete-use="deleteUse" />
    <div class="d-flex justify-content-center">
        <button class="btn btn-primary btn-lg mx-auto" data-bs-toggle="modal" data-bs-target="#CreateUseModal">
            Add a new Uses relationship
        </button>
    </div>

    <div class="modal fade" id="CreateUseModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Add a new uses relationship</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>

                <div class="modal-body">
                    <div>
                        <label for="name" class="form-label">Project ID</label>
                        <select v-model="newUse.project" type="" class="form-control" id="name" placeholder="Name">
                            <option v-for="project in projects" :value="project.id">{{ project.name }}</option>
                        </select>
                    </div>
                    <div>
                        <label for="type" class="form-label">Technology ID</label>
                        <select v-model="newUse.technology" type="text" class="form-control" id="type"
                            placeholder="Type">
                            <option v-for="technology in technologies" :value="technology.id">{{ technology.name }}
                            </option>
                        </select>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary" @click="createUse" data-bs-dismiss="modal">Save
                        changes</button>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
export default {
    components: {
        UsesTable,
    },
    data() {
        return {
            title: 'Uses',
            uses: [],
            projects: [],
            technologies: [],
            newUse: {
                project: '',
                technology: '',
            },
        }
    },
    async mounted() {
        const response = await fetch('http://localhost:8000/api/uses/')
        const data = await response.json()
        console.log(data);
        this.uses = data.uses;
        const responseProjects = await fetch('http://localhost:8000/api/projects/')
        const dataProjects = await responseProjects.json()
        this.projects = dataProjects.projects;
        const responseTechnologies = await fetch('http://localhost:8000/api/technologies/')
        const dataTechnologies = await responseTechnologies.json()
        this.technologies = dataTechnologies.technologies;

        window.addEventListener('DATA_UPDATE', async () => {
            const response = await fetch('http://localhost:8000/api/uses/')
            const data = await response.json()
            console.log(data);
            this.uses = data.uses;
            const responseProjects = await fetch('http://localhost:8000/api/projects/')
            const dataProjects = await responseProjects.json()
            this.projects = dataProjects.projects;
            const responseTechnologies = await fetch('http://localhost:8000/api/technologies/')
            const dataTechnologies = await responseTechnologies.json()
            this.technologies = dataTechnologies.technologies;
        });
    },
    methods: {
        async deleteUse(use) {
            if (confirm(`Are you sure you want to delete use '${use.id}'?`)) {
                const response = await fetch(`http://localhost:8000/api/use/${use.id}`, {
                    method: 'DELETE',
                })
                if (response.ok)
                    this.uses = this.uses.filter(p => p.id !== use.id)
            }
        },
        async createUse() {
            const response = await fetch('http://localhost:8000/api/uses/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.newUse)
            })
            if (response.ok) {
                const newUse = await response.json()
                this.uses.push(newUse)
            }
        },
        async editUse(use) {
            const response = await fetch(`http://localhost:8000/api/use/${use.id}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(use)
            })
            if (response.ok) {
                const updatedUse = await response.json()
                const index = this.uses.findIndex(u => u.id === use.id)
                this.uses.splice(index, 1, updatedUse)
            }
        }
    }
}
</script>