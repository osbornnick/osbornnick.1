<script>
    import Intro from "../components/intro.svelte";
    import Timeline from "../components/timeline.svelte";
    import DarkToggle from "../components/darkToggle.svelte";
    import Projects from "../components/projects.svelte";
    import { onMount } from "svelte";
    let darkMode = "true";
    onMount(() => {
        if (
            window.matchMedia &&
            !window.matchMedia("(prefers-color-scheme: dark").matches
        ) {
            main.classList.remove("dark");
            darkMode = "false";
        } else {
            darkMode = "true";
        }
    });
</script>

<main class:dark={darkMode}>
    <div class="dark:bg-slate-900 dark:text-slate-300">
        <div class="container mx-auto justify-center">
            <div class="flex-row-reverse flex md:w-2/3 mx-auto">
                <DarkToggle bind:checked={darkMode} />
            </div>
            <Intro />
            <div class="md:w-2/3 mx-auto text-center">
                <h1 class="text-2xl font-serif my-20">
                    Curious about me? Read on.
                </h1>
            </div>
            <div class="md:w-2/3 mx-auto m-2">
                <Timeline />
            </div>
            <div class="md:w-5/6 mx-auto m-2">
                <Projects />
            </div>
        </div>
    </div>
</main>
