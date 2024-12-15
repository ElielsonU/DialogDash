class Application {
  #loader;
  #body;

  constructor() {
    this.#loader = document.querySelector(".loader");
    this.#body = document.querySelector("body");
  }

  static init() {
    const app = new Application();
    app.init();
  }

  init() {
    location  
  }
}

Application.init();
