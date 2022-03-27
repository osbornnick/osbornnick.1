<script>
    export let date;
    export let title;
    export let subtitle;
    export let description;
    export let first;
    export let last;
    export let concurrent = false;
    export let branch = false;
    export let merge = false;
    const monthNames = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ];
    $: [month, year] =
        date === "today"
            ? [monthNames[new Date().getMonth()], new Date().getFullYear()]
            : date.split(" ");
    let h, w;
    let line1x;
    let line2x;
    $: line1x = w / 3;
    $: line2x = (w * 2) / 3;

    let timelineColor = "slate-400"; // if changing, update the safelist in tailwind.config.cjs
</script>

<div class="group">
    <div class="flex flex-row">
        <div class="sm:text-right basis-3/12 font-serif my-auto">
            <div class="text-xl">{year}</div>
            <div class="-translate-y-2">{month}</div>
        </div>
        <div
            class="basis-1/12 hidden sm:block"
            bind:offsetHeight={h}
            bind:offsetWidth={w}
        >
            <svg width="100%" height="100%">
                {#if first}
                    <path
                        d="M {line1x} {h / 2} v {h / 2}"
                        class={"stroke-" + timelineColor}
                        stroke-width={w / 13}
                    />
                {:else if last}
                    <path
                        d="M {line1x} {h / 2} v -{h / 2}"
                        class={"stroke-" + timelineColor}
                        stroke-width={w / 13}
                    />
                {:else}
                    <path
                        d="M {line1x} 0 v {h}"
                        class={"stroke-" + timelineColor}
                        stroke-width={w / 13}
                    />
                {/if}
                {#if branch}
                    <path
                        d="M {line1x} {h / 2} C {line1x} {(3 * h) /
                            4} {line2x} {(3 * h) / 4} {line2x} {h}"
                        class={"stroke-" + timelineColor}
                        stroke-width={w / 13}
                        fill="transparent"
                    />
                {/if}
                {#if merge}
                    <path
                        d="M {line2x} 0 C {line2x} {h / 4} {line1x} {h /
                            4} {line1x} {h / 2}"
                        class={"stroke-" + timelineColor}
                        stroke-width={w / 13}
                        fill="transparent"
                    />
                {/if}
                {#if concurrent}
                    <path
                        d="M {line2x} 0 v {h}"
                        class={"stroke-" + timelineColor}
                        stroke-width={w / 13}
                    />
                    <circle
                        cx={line2x}
                        cy={h / 2}
                        r={w / 7}
                        class={"fill-" +
                            timelineColor +
                            " group-hover:scale-125 duration-300"}
                        style="transform-origin: {line2x}px {h / 2}px"
                    />
                {:else}
                    <circle
                        cx={line1x}
                        cy={h / 2}
                        r={w / 7}
                        class={"fill-" +
                            timelineColor +
                            " group-hover:scale-125 duration-300"}
                        style="transform-origin: {line1x}px {h / 2}px"
                    />
                {/if}
                {#if date === "today"}
                    <defs>
                        <linearGradient
                            id="grad"
                            gradientUnits="userSpaceOnUse"
                            x1={line1x}
                            y1={h / 2}
                            x2={line2x}
                            y2={h}
                        >
                            <stop offset="0" stop-color="#94a3b8" />
                            <stop offset=".2" stop-color="#94a3b8" />
                            <stop
                                offset=".65"
                                stop-opacity="0"
                                stop-color="#94a3b8"
                            />
                        </linearGradient>
                    </defs>
                    <path
                        d="M {line1x} {h / 2} L {line1x} {h}"
                        stroke-width={w / 13}
                        stroke="url(#grad)"
                    />
                {/if}
            </svg>
        </div>
        <div
            class="basis-8/12 my-auto origin-left md:group-hover:scale-125 duration-300 py-5"
        >
            <h3 class="text-xl font-serif">{title}</h3>
            <h4 class="italic font-serif">{subtitle}</h4>
            <p>{@html description}</p>
        </div>
    </div>
</div>
