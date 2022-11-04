var noble = require('noble');
noble.startScanning(); // any service UUID, no duplicates


// noble.startScanning([], true); // any service UUID, allow duplicates


// var serviceUUIDs = []; //"<service UUID 1>", ...]; // default: [] => all
// var allowDuplicates = false;  //<false| true >; // default: false

// noble.startScanning(serviceUUIDs, allowDuplicates[, callback(error)]); // particular UUID's
