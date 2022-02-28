<script>
    import Link from "../components/link.svelte";
</script>

<div
    class="flex flex-row justify-evenly md:w-2/3 mx-auto my-10 flex-wrap-reverse"
>
    <div class="font-serif m-5">
        <h1 class="text-2xl italic">Hi, I'm</h1>
        <h1 class="text-4xl">Nick Osborn.</h1>
        <p>I like to write code and bake bread.</p>
        <p>I play piano, D&D, and climb rocks.</p>
        <p>
            You can find me on <Link href="https://github.com/osbornnick/"
                >github</Link
            >.
        </p>
    </div>
    <img src={"/me-circle.png"} alt="me smiling" class="m-5 w-48" />
</div>
