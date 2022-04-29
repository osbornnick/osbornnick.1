<script>
    export let title;
    export let description;
    export let link;
    export let image;
    export let github;
    export let tech;
    export let date;
    import GithubIcon from "./githubIcon.svelte";
    import ArrowIcon from "./arrowIcon.svelte";
</script>

<div class="p-8 flex">
    <div class={image ? "md:w-1/2" : ""}>
        <h1 class="text-xl font-serif flex">
            {title}
            {#if github}
                <a href={github} class="self-center">
                    <GithubIcon
                        classes="dark:fill-slate-300 ml-2 p-0 hover:fill-slate-600 dark:hover:fill-slate-100"
                    />
                </a>
            {/if}
        </h1>
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
        {#if link}
            <a class=" text-sm flex group" href={link}>
                VISIT {title.toUpperCase()}
                <ArrowIcon
                    stroke="dark:stroke-white stroke-black"
                    fill="dark:fill-white fill-black"
                    classes="self-center ml-2 group-hover:translate-x-4 duration-200"
                />
            </a>
        {/if}
    </div>
    {#if image}
        <div class="hidden md:block my-auto w-1/2">
            <img src={image} alt="project screenshot" class="rounded-md" />
        </div>
    {/if}
</div>

<style>
</style>
