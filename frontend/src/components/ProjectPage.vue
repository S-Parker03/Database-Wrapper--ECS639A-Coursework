<script setup>
    import { ref } from 'vue'
    import ProjectTable from './ProjectTable.vue'
</script>

<template>
    <ProjectTable
        :projects="projects"
        @edit-project= "editProject"
        @delete-project="deleteProject"
     />
    <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#CreateProjectModal">
        Add a new Project
    </button>

    <div class="modal fade" id="CreateProjectModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="exampleModalLabel">Add a new project</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>

            <div class="modal-body">
                <div>
                    <label for="name" class="form-label">Project Name</label>
                    <input v-model="newProject.name" type="text" class="form-control" id="name" placeholder="Name">
                </div>
                <div>
                    <label for="type" class="form-label">Project Type</label>
                    <input v-model="newProject.type" type="text" class="form-control" id="type" placeholder="Type">
                </div>
                <div>
                    <label for="date" class="form-label">Project Date</label>
                    <input v-model="newProject.date" type="date" class="form-control" id="date" placeholder="Date">
                </div>
                <div>
                    <label for="description" class="form-label">Project Description</label>
                    <textarea v-model="newProject.description" class="form-control" id="description" rows="3"></textarea>
                </div>  
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary" @click="createProject" data-bs-dismiss="modal">Save changes</button>
            </div>
            </div>
        </div>
    </div>
</template>


<script>
export default {
    components: {
        ProjectTable,  
    },
    data() {
        return {
            title: 'Projects',
            projects: [],
            newProject: {
                name: '',
                type: '',
                date: '',
                description: ''
            },
        }
    },
    async mounted() {
        const response = await fetch('http://localhost:8000/api/projects/')
        const data = await response.json()
        this.projects = data.projects;
    },
    methods: {
        async deleteProject(project) {
            if (confirm(`Are you sure you want to delete the '${project.name}' project?`)) {
                const response = await fetch(`http://localhost:8000/api/project/${project.id}`, {
                    method: 'DELETE',
                })
                if (response.ok)
                    this.projects = this.projects.filter(p => p.id !== project.id)
                    window.dispatchEvent(new Event('DATA_UPDATE'))
            }
        },
        async createProject(){
            const response = await fetch('http://localhost:8000/api/projects/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.newProject)
                })
            if (response.ok){
                const newProject = await response.json()
                this.projects.push(newProject)
                window.dispatchEvent(new Event('DATA_UPDATE'))
            }
        },   
        async editProject(project){
            const response = await fetch(`http://localhost:8000/api/project/${project.id}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(project)
                })
            if (response.ok){
                const updatedProject = await response.json()
                const index = this.projects.findIndex(p => p.id === project.id)
                this.projects.splice(index, 1, updatedProject)
                window.dispatchEvent(new Event('DATA_UPDATE'))
            }
        }
    }
}
</script>