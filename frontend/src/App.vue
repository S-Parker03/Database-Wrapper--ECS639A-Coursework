<script setup>
import { ref } from 'vue'
import ProjectPage from './components/ProjectPage.vue'
import TechnologyPage from './components/TechnologyPage.vue'
import UsesPage from './components/UsesPage.vue'
</script>

<template>
    <header class="h2 w-100 m-0 p-0" style="background-color:#f3f3f3;">
        <ul class="nav nav-tabs">
            <li class="nav-item">
                <button class="nav-link active" id="projects-tab" data-bs-toggle="tab"
                    data-bs-target="#projects-tab-pane" type="button" role="tab" aria-controls="projects-tab-pane"
                    aria-selected="true">Projects</button>
            </li>
            <li class="nav-item">
                <button class="nav-link" id="tech-tab" data-bs-toggle="tab" data-bs-target="#tech-tab-pane"
                    type="button" role="tab" aria-controls="tech-tab-pane" aria-selected="false">Technologies</button>
            </li>
            <li class="nav-item">
                <button class="nav-link" id="uses-tab" data-bs-toggle="tab" data-bs-target="#uses-tab-pane"
                    type="button" role="tab" aria-controls="uses-tab-pane" aria-selected="false">Uses</button>
            </li>
        </ul>
    </header>
    <div class="tab-content" id="myTabContent">
        <div class="tab-pane fade show active" id="projects-tab-pane" role="tabpanel" aria-labelledby="projects-tab"
            tabindex="0">
            <ProjectPage />
        </div>
        <div class="tab-pane fade" id="tech-tab-pane" role="tabpanel" aria-labelledby="tech-tab" tabindex="0">
            <TechnologyPage />
        </div>
        <div class="tab-pane fade" id="uses-tab-pane" role="tabpanel" aria-labelledby="uses-tab" tabindex="0">
            <UsesPage />
        </div>
    </div>
</template>
