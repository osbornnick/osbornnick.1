module.exports = {
    content: ["./src/**/*.{html,js,svelte,ts}"],
    theme: {
        fontFamily: {
            sans: ["Graphik", "sans-serif"],
            serif: ["Merriweather", "serif"],
            mono: ["Anonymous Pro", "mono"],
        },
        extend: {},
    },
    plugins: [],
    darkMode: "class",
    purge: {
        options: {
            safelist: ["stroke-slate-400", "fill-slate-400"],
        },
    },
};
