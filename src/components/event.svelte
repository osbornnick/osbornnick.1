<script>
    export let date;
    export let title;
    export let subtitle;
    export let description;
    export let first;
    export let last;

    const [month, year] = date.split(" ");
    let h, w;
</script>

<div class="hoverable">
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
                        d="M {w / 2} {h / 2} v {h / 2}"
                        class="stroke-slate-400"
                        stroke-width={w / 13}
                    />
                {:else if last}
                    <path
                        d="M {w / 2} {h / 2} v -{h / 2}"
                        class="stroke-slate-400"
                        stroke-width={w / 13}
                    />
                {:else}
                    <path
                        d="M {w / 2} 0 v {h}"
                        class="stroke-slate-400"
                        stroke-width={w / 13}
                    />
                {/if}
                <circle
                    cx={w / 2}
                    cy={h / 2}
                    r={w / 7}
                    class="fill-slate-400"
                />
            </svg>
        </div>
        <div class="basis-8/12 my-auto info">
            <h3 class="text-xl font-serif">{title}</h3>
            <h4 class="italic font-serif">{subtitle}</h4>
            <p>{@html description}</p>
        </div>
    </div>
</div>

<style>
    .hoverable:hover .info {
        transform: scale(1.1) translateX(35px);
    }

    .info {
        transition: transform 0.3s;
    }

    .hoverable:hover circle {
        transform: scale(1.5);
        transform-origin: 50% 50%;
        transform-box: fill-box;
    }
    circle {
        transition: transform 0.3s;
        transform-origin: 50% 50%;
    }
</style>
