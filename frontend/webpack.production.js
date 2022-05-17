/* eslint-disable import/no-extraneous-dependencies */
const {merge} = require("webpack-merge");

const CssMinimizerPlugin = require("css-minimizer-webpack-plugin");
const {BundleAnalyzerPlugin} = require("webpack-bundle-analyzer");

const TerserPlugin = require("terser-webpack-plugin");

const common = require("./webpack.common");

module.exports = merge(common, {
    stats: "errors-warnings",
    optimization: {
        minimizer: [
            new TerserPlugin({
                parallel: true,
                terserOptions: {
                    ecma: 11,
                },
            }),
            new CssMinimizerPlugin({}),
        ],
    },
    plugins: [
        new BundleAnalyzerPlugin({
            analyzerMode: "static",
            openAnalyzer: false,
        }),
    ],
});
