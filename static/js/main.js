document.addEventListener('DOMContentLoaded', function() {
    const audioPlayers = document.querySelectorAll('audio');
    
    // Add debug logging and fallback for audio players
    audioPlayers.forEach(player => {
        player.addEventListener('play', function() {
            console.log('Playing audio:', this.querySelector('source').src);
            
            // Pause other players when one starts playing
            audioPlayers.forEach(otherPlayer => {
                if (otherPlayer !== player && !otherPlayer.paused) {
                    otherPlayer.pause();
                }
            });
        });
        
        // Handle errors with fallback
        player.addEventListener('error', function(e) {
            console.error('Audio error:', e);
            const sources = this.querySelectorAll('source');
            let currentSource = 0;
            
            const tryNextSource = () => {
                currentSource++;
                if (currentSource < sources.length) {
                    console.log('Trying next source:', sources[currentSource].src);
                    player.load(); // Reload with new source
                    player.play().catch(e => {
                        console.error('Failed to play alternate source:', e);
                        tryNextSource();
                    });
                } else {
                    console.error('All sources failed');
                    const songTitle = this.closest('.song-card').querySelector('h5').textContent;
                    this.closest('.audio-player').innerHTML = 
                        `<div class="alert alert-danger py-2 mb-0">Failed to play: ${songTitle}</div>`;
                }
            };
            
            tryNextSource();
        }, true); // Use capture to get the event
    });
});