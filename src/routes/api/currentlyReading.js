export async function get() {
    const reading = "reading text";
    return {
        body: { reading },
    };
}
