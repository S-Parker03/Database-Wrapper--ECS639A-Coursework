<template>
   <table>
      <thead>
         <tr>
            <th>#</th>
            <th>Project Name</th>
            <th>Project Type</th>
            <th>Project Date</th>
            <th>Project Description</th>
            <th>Project Completed?</th>
            <th>Actions</th>
         </tr>
      </thead>
      <tbody>
         <tr v-for="(project, index) in projects">
            <th>{{ project.id }}</th>
            <td>{{ project.name }}</td>
            <td>{{ project.type }}</td>
            <td>{{ project.date }}</td>
            <td>{{ project.description }}</td>
            <td>{{ project.completed }}</td>
            <td>
                <button class="btn btn-primary" @click="setEditProject(project)" data-bs-toggle="modal" data-bs-target="#EditProjectModal">
                    Edit
                </button>
                <button class="btn btn-danger" @click="$emit('delete-project', project)">
                    Delete
                </button>
            </td>
         </tr>
      </tbody>
   </table>

   
   <div class="modal fade" id="EditProjectModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="exampleModalLabel">Edit This Project</h1>
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
                <div>
                    <label for="completed" class="form-label">Project Completed?</label>
                    <select v-model="newProject.completed" class="form-control" id="description" rows="3">
                        <option :value= true >Completed</option>
                        <option :value= false >Not Completed</option>
                    </select>
                </div>     
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary" @click="editProject" data-bs-dismiss="modal">Save changes</button>
            </div>
            </div>
        </div>
    </div>
</template>   


<script>
   export default{
      emits: ['edit-project', 'delete-project'],
      props: {
         projects:{
            type: Array
         }
      },
      data(){
         return{
            newProject:{
               name: '',
               type: '',
               date: '',
               description: ''
            }
         }
      },
      methods:{
         setEditProject(project) {
            this.newProject = { ...project };
         },
         editProject() {
            this.$emit('edit-project', this.newProject)
         }
      }
   }
</script>

