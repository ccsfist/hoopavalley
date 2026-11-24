# Exercise 4: HVTcoordinate Responses

## This map shows what shelters offer.  

- **Click on "Needs" to see what people needed**

- **click on <-Results to see the gap between what people need and what is offeed**

- If you go again, could you better align needs and what is offered?

- Are there chances it could get worse if you dont update the communication?

- How might you use versions of this before, during a disaster?
<style>
  .live-frame { position: relative; height: 90vh; }
  .live-frame iframe { width: 100%; height: 100%; border: none; }
  .live-frame .live-loading {
    position: absolute; inset: 0; z-index: 2;
    display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 1rem;
    background: #fff; color: #555; font-size: 0.9rem;
    transition: opacity 0.5s;
  }
  .live-frame .live-loading.done { opacity: 0; pointer-events: none; }
  .live-frame .live-spinner {
    width: 40px; height: 40px;
    border: 4px solid #ddd; border-top-color: #555; border-radius: 50%;
    animation: live-spin 0.9s linear infinite;
  }
  @keyframes live-spin { to { transform: rotate(360deg); } }
</style>

<div class="live-frame">
  <div class="live-loading">
    <div class="live-spinner"></div>
    <div>Loading live results…</div>
  </div>
  <iframe
    src="https://twowaydisplay.streamlit.app/?game=Coordinate&amp;map=pies&amp;show=offers&amp;view=all&amp;embed=true"
    onload="var o=this.previousElementSibling; setTimeout(function(){ o.classList.add('done'); }, 2000);">
  </iframe>
</div>


<div id="slide-config" data-type="start" data-next="../hoopavalleynetwork/"> </div>
