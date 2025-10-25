// Fondo animado con partículas
(function () {
  const canvas = document.getElementById("bg");
  const ctx = canvas.getContext("2d");
  let w = canvas.width = innerWidth;
  let h = canvas.height = innerHeight;
  const particles = [];
  const count = Math.floor((w * h) / 70000);

  function rand(min, max) { return Math.random() * (max - min) + min; }

  function Particle() {
    this.x = rand(0, w);
    this.y = rand(0, h);
    this.vx = rand(-0.2, 0.2);
    this.vy = rand(-0.2, 0.2);
    this.r = rand(0.6, 1.6);
    this.alpha = rand(0.05, 0.25);
  }

  Particle.prototype.draw = function () {
    ctx.beginPath();
    ctx.fillStyle = "rgba(0,230,255," + this.alpha + ")";
    ctx.arc(this.x, this.y, this.r, 0, Math.PI * 2);
    ctx.fill();
  }

  function init() {
    particles.length = 0;
    for (let i = 0; i < count; i++) particles.push(new Particle());
  }

  function anim() {
    ctx.clearRect(0, 0, w, h);
    for (let p of particles) {
      p.x += p.vx;
      p.y += p.vy;
      if (p.x < -10) p.x = w + 10;
      if (p.x > w + 10) p.x = -10;
      if (p.y < -10) p.y = h + 10;
      if (p.y > h + 10) p.y = -10;
      p.draw();
    }
    requestAnimationFrame(anim);
  }

  addEventListener("resize", () => {
    w = canvas.width = innerWidth;
    h = canvas.height = innerHeight;
    init();
  });

  init();
  anim();
})();
