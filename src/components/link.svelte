<script>
    export let href;
    const colors = ["#fada5e", "#5eccfa", "#8c5efa"];
    let color;
    $: color;
    import { onMount } from "svelte";

    onMount(() => {
        color = colors[Math.floor(Math.random() * colors.length)];
    });
</script>

<a
    class="dark:text-slate-300 underline underline-offset-2 hover:text-blue-500 dark:hover:text-blue-500"
    {href}><slot /></a
>

<style>
    /* a {
        background-color: transparent;
        transition: box-shadow 200ms;
        transition-timing-function: cubic-bezier(0.18, 0.89, 0.32, 1.28);
        box-shadow: 0 -3px 0 0 inset;
    }
    a:hover {
        box-shadow: 0 -10px 0 0 inset;
    } */
</style>
