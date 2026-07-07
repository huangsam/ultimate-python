import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://sambyte.net',
  base: '/ultimate-python',
  output: 'static',
  prefetch: {
    defaultStrategy: 'hover'
  }
});
