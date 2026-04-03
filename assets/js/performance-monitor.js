// performance-monitor.js

// Function to log performance metrics
function logPerformanceMetrics() {
    // Record the user timing metrics
    const performanceMetrics = window.performance.getEntriesByType('navigation');
    console.log('Navigation Timing:', performanceMetrics);

    // Log Web Vitals metrics
    if(window.PerformanceObserver) {
        new PerformanceObserver((entryList) => {
            entryList.getEntries().forEach(entry => {
                console.log('Web Vital:', entry);
            });
        }).observe({type: 'paint', buffered: true});
    }

    // Resource Timing Analysis
    const resources = performance.getEntriesByType('resource');
    console.log('Resource Timing:', resources);
}

// Call the logging function after the window load event
window.addEventListener('load', logPerformanceMetrics);