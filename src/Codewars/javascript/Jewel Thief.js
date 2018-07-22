var crack = function (safe) {
    code = ""
    unlocking = "click"
    for (let i = 0; i < 3; ++i) {
        for (let i = 0; i < 100; ++i) {
            let num = i < 10 ? "0" + i : i;
            for (let direction of ["L", "R"]) {
                comb = direction + num;
                if (safe.unlock(code + comb) == unlocking) {
                    code += comb;
                }
            }
        }
        unlocking += "-click"
        code += "-"
    }
    safe.unlock(code.substring(0, 11))
    return safe.open();
}