<script>
    import data from "../../static/timeline.json";
    import Event from "./event.svelte";
    import { onMount } from "svelte";
    onMount(() => {
        data.timeline[0].first = true;
        data.timeline[data.timeline.length - 1].last = true;
        data.timeline.reverse();
        data.timeline.forEach((evt, i) => {
            if (evt.concurrent) {
                if (i - 1 > -1)
                    data.timeline[i - 1] = {
                        ...data.timeline[i - 1],
                        branch: true,
                    };
                if (i + 1 < data.timeline.length)
                    data.timeline[i + 1] = {
                        ...data.timeline[i + 1],
                        merge: true,
                    };
            }
        });
    });
</script>

<h1 class="text-2xl font-serif mb-5 sm:mb-0 ml-2">Professional Timeline</h1>
<div class="space-y-1 sm:space-y-0 ml-5 md:ml-0">
    {#each data.timeline as event, i}
        <Event {...event} />
    {/each}
</div>
