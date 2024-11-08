<template>
    <thead>
        <tr>
            <th>#</th>
            <th>Technology Name</th>
            <th>Technology Type</th>
            <th>Technology Description</th>
            <th>Technology Version</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        <tr v-for="(technology, index) in technologies">
            <th>{{ technology.id }}</th>
            <td>{{ technology.name }}</td>
            <td>{{ technology.type }}</td>
            <td>{{ technology.description }}</td>
            <td>{{ technology.version }}</td>
            <td>
                <button class="btn btn-primary" @click="setEditTechnology(technology)" data-bs-toggle="modal" data-bs-target="#EditTechnologyModal">
                    Edit
                </button>
                <button class="btn btn-danger" @click="$emit('delete-technology', technology)">
                    Delete
                </button>
            </td>
        </tr>
    </tbody>

    <div class="modal fade" id="EditTechnologyModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="exampleModalLabel">Edit This Technology</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>

            <div class="modal-body">
                <div>
                    <label for="name" class="form-label">Technology Name</label>
                    <input v-model="newTechnology.name" type="text" class="form-control" id="name" placeholder="Name">
                </div>
                <div>
                    <label for="type" class="form-label">Technology Type</label>
                    <input v-model="newTechnology.type" type="text" class="form-control" id="type" placeholder="Type">
                </div>
                <div>
                    <label for="description" class="form-label">Technology Description</label>
                    <textarea v-model="newTechnology.description" class="form-control" id="description" rows="3"></textarea>
                </div>
                <div>
                    <label for="version" class="form-label">Technology Version</label>
                    <input v-model="newTechnology.version" type="text" class="form-control" id="version" placeholder="Version">
                </div> 
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary" @click="editTechnology" data-bs-dismiss="modal">Save changes</button>
            </div>
            </div>
        </div>
    </div>
</template>

<script>
   export default{
        emits: ['edit-technology', 'delete-technology'],
        props:{
            technologies:{
                type: Array
            }
        },
        data(){
            return{
                newTechnology:{
                    name: '',
                    type: '',
                    date: '',
                    description: ''
                }
            }
        },
        methods:{
            setEditTechnology(technology) {
                this.newTechnology = { ...technology };
            },
            editTechnology() {
                this.$emit('edit-technology', this.newTechnology)
            }
        }
    }
</script>