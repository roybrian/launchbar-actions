'use strict';
const lb = require('launchbar-node');

(async () => {
    const text = process.argv[2].toLowerCase()
    if (lb.options.commandKey) {
        return console.log(text);
    } else {
        return await lb.paste(text);
    }
})();