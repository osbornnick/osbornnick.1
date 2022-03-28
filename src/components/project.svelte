<script>
    export let title;
    export let description;
    export let link;
    export let image;
    export let github;
    export let tech;
    export let date;
</script>

<div class="m-3 p-5 flex">
    <div class={image ? "md:w-1/2" : ""}>
        <h1 class="text-xl font-serif">
            {title}
        </h1>
        <!-- <img src="/GitHub-Mark-32px.png" alt="source" class="w-6" /> -->
        <ul class="flex flex-wrap py-2">
            {#each tech as t, i}
                <li class="pr-2">
                    <a
                        href={t.link}
                        class="underline decoration-blue-500 hover:text-blue-500 dark:decoration-blue-700 font-mono"
                        >{t.name}</a
                    >
                </li>
            {/each}
        </ul>
        <p class="pb-6 pr-6 text-sm">{@html description}</p>
        <div class="flex flex-wrap">
            {#if link}
                <a
                    href={link}
                    class="p-4 mx-2 border rounded-lg border-blue-500 font-serif text-blue-500 hover:bg-blue-500 hover:text-white duration-150"
                    >Visit {title}</a
                >
            {/if}
            {#if github}
                <a
                    class="p-4 mx-2 border rounded-lg font-serif border-emerald-500 text-emerald-500 hover:bg-emerald-500 hover:text-white duration-150"
                    href={github}>View source</a
                >
            {/if}
        </div>
    </div>
    {#if image}
        <div class="hidden md:block my-auto w-1/2">
            <img src={image} alt="project screenshot" class="rounded-md" />
        </div>
    {/if}
</div>

<style>
</style>
