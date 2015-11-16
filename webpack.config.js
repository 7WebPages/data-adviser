module.exports = {
    context: __dirname + "/src/analytics/analytics/js",
    entry: "core/core",
    output: {
        path: __dirname + "/src/analytics/analytics/static/build",
        filename: "bundle.js"
    }
}