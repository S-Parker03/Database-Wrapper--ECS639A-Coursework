<template>
    <table class="table">
        <caption>List of Uses Relationships</caption>
        <thead>
            <tr>
                <th scope="col">#</th>
                <th scope="col">Project ID</th>
                <th scope="col">Technology ID</th>
                <th scope="col">Actions</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(use, index) in uses">
                <th scope="row">{{ use.id }}</th>
                <td>{{ use.project }}</td>
                <td>{{ use.technology }}</td>
                <td>
                    <button class="btn btn-primary" @click="setEditUse(use)" data-bs-toggle="modal"
                        data-bs-target="#EditUseModal">
                        Edit
                    </button>
                    <button class="btn btn-danger" @click="$emit('delete-use', use)">
                        Delete
                    </button>
                </td>
            </tr>
        </tbody>
    </table>

    <div class="modal fade" id="EditUseModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Edit This Use</h1>
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
                    <button type="button" class="btn btn-primary" @click="editUse" data-bs-dismiss="modal">Save
                        changes</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    emits: ['edit-use', 'delete-use'],
    props: {
        uses: {
            type: Array
        },
        projects: {
            type: Array
        },
        technologies: {
            type: Array
        }
    },
    data() {
        return {
            newUse: {
                project: '',
                technology: '',
            }
        }
    },
    methods: {
        setEditUse(use) {
            this.newUse = { ...use }
        },
        editUse() {
            this.$emit('edit-use', this.newUse);
        }
    }
}
</script>
