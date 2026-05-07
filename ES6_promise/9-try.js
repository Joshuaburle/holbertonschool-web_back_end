export default function guardrail(mathFunction) {
    let queue = [];
    try {
        const result = mathFunction();
        queue.push(result);
    } catch (error) {
        queue.push(error.toString());
    }
    queue.push("Guardrail was processed");
    return queue;
}
