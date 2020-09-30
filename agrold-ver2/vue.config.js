const path = require('path');

if( process.env.NODE_ENV === "production") {
  module.exports = {
    assetsDir: '../../static',
    publicPath: '',
    publicPath: undefined,
    outputDir: path.resolve(__dirname, '../templates/vue_template'),
    runtimeCompiler: undefined,
    productionSourceMap: undefined,
    parallel: undefined,
    css: undefined
  };
}
