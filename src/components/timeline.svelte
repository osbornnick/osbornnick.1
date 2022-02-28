<script>
    import data from "../../static/timeline.json";
    import Event from "./event.svelte";
</script>

<h1 class="text-2xl font-serif mb-5 sm:mb-0">Professional Timeline</h1>
<div class="space-y-5 sm:space-y-0">
    {#each data.timeline as event, i}
        <Event
            {...event}
            first={i === 0}
            last={i === data.timeline.length - 1}
        />
    {/each}
</div>
