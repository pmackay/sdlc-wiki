// Copied over Quartz's own quartz.ts at build time (see .github/workflows/deploy.yml).
// Keeps the stock config/layout loading and adds one TS-only override: the
// Explorer sidebar mixes lowercase folder slugs ("capability") and tool-styled
// page titles ("gstack", "bd create"), so capitalise the first character of every
// sidebar label. Only the sidebar changes; page headings keep their real casing.
// mapFn is serialised and run in the browser, so it must stay self-contained.
// Overrides must be registered before loadQuartzConfig() runs.
import { componentRegistry } from "./quartz/components/registry"
import { loadQuartzConfig, loadQuartzLayout } from "./quartz/plugins/loader/config-loader"

componentRegistry.setOptionOverrides("@quartz-community/explorer", {
  mapFn: (node: { displayName: string }) => {
    const name = node.displayName
    if (name) node.displayName = name.charAt(0).toUpperCase() + name.slice(1)
    return node
  },
})

const config = await loadQuartzConfig()
export default config
export const layout = await loadQuartzLayout()
