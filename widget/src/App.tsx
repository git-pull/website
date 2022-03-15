import React from "react";
import "./App.css";

function App() {
  return (
    <div id="git-pull-projects">
      <h1 className="title">
        TONY NARLOCK <small>/ team git-pull</small>
      </h1>
      <div>
        <h2>vcs-python</h2> <a href="https://vcspull.git-pull.com/">vcspull</a> (
        <a href="https://libvcs.git-pull.com/">libvcs</a>, <a href="https://g.git-pull.com/">g</a>)
      </div>
      <div>
        <h2>tmux-python</h2> <a href="https://tmuxp.git-pull.com/">tmuxp</a> (
        <a href="https://libtmux.git-pull.com/">libtmux</a>)
      </div>
      <div>
        <h2>cihai</h2>
        <div className="indent">
          <div>
            <a href="https://unihan-etl.git-pull.com/">unihan-etl</a> (
            <a href="https://unihan-db.git-pull.com/">db</a>)
          </div>
          <div>
            <a href="https://cihai.git-pull.com/">cihai</a> (
            <a href="https://cihai-cli.git-pull.com/">cli</a>)
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
