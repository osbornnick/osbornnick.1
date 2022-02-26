<script>
    import CurrentlyReading from "../components/CurrentlyReading.svelte";
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
                    You can find me on <a href="https://github.com/osbornnick/"
                        >github</a
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
    <CurrentlyReading />
</main>

<style>
    a {
        color: black;
        background-color: transparent;
        /* box-shadow: 0 -3px 0 0 #FADA5E inset; */
        transition: box-shadow 200ms;
        transition-timing-function: cubic-bezier(0.18, 0.89, 0.32, 1.28);
        box-shadow: 0 -3px 0 0 #fada5e inset;
    }
    a:hover {
        box-shadow: 0 -10px 0 0 #fada5e inset;
    }
</style>
