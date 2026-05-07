export default function cleanSet(set, startString) {
    if (!(set instanceof Set) || typeof startString !== 'string' || startString === '') {
        return '';
    }
    return [...set]
        .filter(value => value.startsWith(startString))
        .map(value => value.slice(startString.length))
        .join('-');
};
