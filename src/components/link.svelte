<script>
    export let href;
    // const colors = ["#FADA5E", "#5ECCFA", "#8C5EFA"];
    // let color;
    // $: color;
    // import { onMount } from "svelte";

    // onMount(() => {
    //     color = colors[Math.floor(Math.random() * colors.length)];
    // });
</script>

<a class="font-bold" {href}><slot /></a>

<style>
    a {
        background: linear-gradient(to right, #30cfd0, #c43ad6);
        background-clip: text;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* old styling */
    /* a {
        background-color: transparent;
        transition: box-shadow 200ms;
        transition-timing-function: cubic-bezier(0.18, 0.89, 0.32, 1.28);
        box-shadow: 0 -3px 0 0 var(--color) inset;
    }
    a:hover {
        box-shadow: 0 -10px 0 0 var(--color) inset;
    } */
</style>
