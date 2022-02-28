<script>
    import Link from "../components/link.svelte";
    ("");
</script>

<main class="flex items-center flex-col">
    <div class="flex flex-row justify-evenly w-1/2">
        <div class="flex items-center">
            <div>
                <h1 class="font-serif text-2xl italic">Hi, I'm</h1>
                <h1 class="font-serif text-4xl">Nick Osborn.</h1>
                <p class="font-serif">I like to write code and bake bread.</p>
                <p class="font-serif">I play piano and ultimate frisbee.</p>
                <p class="font-serif">
                    You can find me on <Link
                        href="https://github.com/osbornnick/">github</Link
                    >.
                </p>
            </div>
        </div>
        <img
            src={"../static/me-circle.png"}
            alt="me smiling"
            class="m-5 w-1/3"
        />
    </div>
</main>

<style>
</style>
