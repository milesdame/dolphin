        // Zoom and pan code based on D3 tutorial available at: https://www.d3indepth.com/zoom-and-pan/
        let zoom = d3.zoom()
            .scaleExtent([.1, 4])
            .translateExtent([[-1246.3125, 0], [2492.625, 1492.6582]])
            .on('zoom', handleZoom);

        function handleZoom(e) {
            d3.select('svg g')
                .attr('transform', e.transform);
        }

        function initZoom() {
            d3.select('svg')
                .call(zoom);
        }

        initZoom();