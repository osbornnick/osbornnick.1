<script>
    import data from "../../static/projects.json";
    import Project from "./project.svelte";
</script>

<h1 class="text-2xl font-serif md:mb-5 mb-0 ml-2">Projects</h1>
<div class="">
    {#each data.projects as project, i}
        <Project {...project} />
    {/each}
</div>
