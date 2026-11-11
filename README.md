# IA STAFF Studio — Open Source

**L'humain dirige. Les intelligences collaborent.**

Dépôt public de modèles configurables IA STAFF, de CLI Python/TypeScript et de workflows de référence pour des déploiements sur Vercel.

## Structure

- `catalog/` : catalogue de modèles.
- `templates/distributions/` : Persona, Agent supervisé, Blog avec assistant, Light, Medium, Pro, Entreprise.
- `templates/web-nextjs/` : application Next.js minimale.
- `cli/python/` et `cli/typescript/` : outils d'initialisation.
- `workflows/` : définitions JSON d'exemple, **non exécutables** directement.
- `schemas/` : contrat de distribution JSON.
- `tests/` et `.github/workflows/` : contrôles qualité.
- `docs/` : architecture et sécurité.

## Démarrer

```bash
python3 cli/python/ia_staff.py list
python3 cli/python/ia_staff.py init persona /tmp/mon-persona
cd /tmp/mon-persona
npm install
npm run build
npm run dev
```

Pour TypeScript :

```bash
cd cli/typescript
npm install
npm run build
node dist/index.js list
node dist/index.js init blog /tmp/mon-blog
```

Chaque manifeste décrit des **objectifs de configuration**, pas des fonctionnalités déjà déployées. Le starter ne fournit pas de LLM, de base de données, d'authentification ou d'exécution des workflows. Chaque service demande une intégration et des tests supplémentaires.

La compilation Next.js n'effectue aucune migration ni seed. Les secrets restent côté serveur. Les actions externes des futurs agents nécessiteront une autorisation et une supervision humaines.

Voir [English documentation](README.en.md), [architecture](docs/architecture.md), [security](docs/security.md) et [Vercel deployment](docs/vercel.md).

Licence [MIT](LICENSE).
