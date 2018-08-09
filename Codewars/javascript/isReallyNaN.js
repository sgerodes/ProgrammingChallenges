const isReallyNaN = (val) => {
    return String(val) === "NaN" && typeof val !== "string";
};