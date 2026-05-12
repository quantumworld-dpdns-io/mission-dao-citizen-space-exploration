# ---- Dev ----
FROM node:20-alpine AS dev
WORKDIR /app
COPY web/package.json web/ ./
RUN npm install
EXPOSE 3000
CMD ["npm", "run", "dev"]

# ---- Build ----
FROM node:20-alpine AS build
WORKDIR /app
COPY web/ ./
RUN npm ci && npm run build

# ---- Prod ----
FROM node:20-alpine AS prod
WORKDIR /app
COPY --from=build /app/.next/standalone ./
COPY --from=build /app/.next/static ./.next/static
COPY --from=build /app/public ./public
EXPOSE 3000
CMD ["node", "server.js"]
