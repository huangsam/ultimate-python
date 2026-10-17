/**
 * Registers a setup callback that runs on initial page load and after every
 * Astro View Transitions navigation (`astro:page-load`).
 *
 * Provides an `AbortSignal` that is automatically aborted before each DOM swap
 * (`astro:before-swap`) or re-initialization, ensuring any event listeners
 * registered with `{ signal }` are cleanly torn down without duplicates.
 */
export function mountOnPageLoad(setup: (signal: AbortSignal) => void): void {
  let controller: AbortController | null = null;

  const cleanup = () => {
    if (controller) {
      controller.abort();
      controller = null;
    }
  };

  const run = () => {
    cleanup();
    controller = new AbortController();
    setup(controller.signal);
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', run, { once: true });
  } else {
    run();
  }

  document.addEventListener('astro:after-swap', run);
  document.addEventListener('astro:page-load', run);
  document.addEventListener('astro:before-swap', cleanup);
}
