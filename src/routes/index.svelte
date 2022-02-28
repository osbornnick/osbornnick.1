<script>
    import Link from "../components/link.svelte";
    import Timeline from "../components/timeline.svelte";
    import { faArrowDown } from "@fortawesome/free-solid-svg-icons";
    import { FontAwesomeIcon } from "fontawesome-svelte";
</script>

<main class="container mx-auto justify-center">
    <div
        class="flex flex-row justify-evenly w-2/3 mx-auto my-10 flex-wrap-reverse"
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
        <img
            src={"../static/me-circle.png"}
            alt="me smiling"
            class="m-5 w-48"
        />
    </div>
    <div class="w-2/3 mx-auto text-center">
        <h1 class="text-2xl font-serif my-20">
            Curious about me? Read on.
            <FontAwesomeIcon
                icon={faArrowDown}
                size="xl"
                class="text-sky-700"
            />
        </h1>
    </div>
    <div class="w-2/3 mx-auto">
        <Timeline />
    </div>
</main>
