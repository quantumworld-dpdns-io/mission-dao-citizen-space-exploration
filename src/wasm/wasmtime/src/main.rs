use anyhow::Result;
use std::path::Path;
use wasmtime::{Engine, Linker, Module, Store};
use wasmtime_wasi::{WasiCtxBuilder, WasiCtx, add_to_linker};

#[tokio::main]
async fn main() -> Result<()> {
    let engine = Engine::default();
    let wasi_ctx = WasiCtxBuilder::new()
        .inherit_stdio()
        .inherit_args()?
        .build();
    let mut store = Store::new(&engine, wasi_ctx);
    let mut linker: Linker<WasiCtx> = Linker::new(&engine);
    add_to_linker(&mut linker, |s| s)?;

    let plugin_dir = Path::new("plugins");
    if plugin_dir.exists() {
        for entry in std::fs::read_dir(plugin_dir)? {
            let entry = entry?;
            let path = entry.path();
            if path.extension().map_or(false, |e| e == "wasm") {
                let module = Module::from_file(&engine, &path)?;
                let instance = linker.instantiate(&mut store, &module)?;
                let run = instance.get_typed_func::<(), i32>(&mut store, "_start")?;
                let result = run.call(&mut store, ())?;
                println!("Plugin {} exited with code {}", path.display(), result);
            }
        }
    }
    Ok(())
}
