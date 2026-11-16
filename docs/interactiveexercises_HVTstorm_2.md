# Exercise 1: HVTstorm Responses

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
    src="https://twowaydisplay.streamlit.app/?game=disasterlistplaceholder&amp;view=all&amp;present=1&amp;embed=true"
    onload="var o=this.previousElementSibling; setTimeout(function(){ o.classList.add('done'); }, 2000);">
  </iframe>
</div>


<div id="slide-config" data-type="start" data-next="../interactiveexercises_HVTalert_1/"> </div>
