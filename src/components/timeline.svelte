<script>
    import data from "../../static/timeline.json";
    import Event from "./event.svelte";
</script>

{#each data.timeline as event, i}
    <Event {...event} first={i === 0} last={i === data.timeline.length - 1} />
{/each}
