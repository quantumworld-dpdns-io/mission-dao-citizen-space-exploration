import { ethers } from "hardhat";

async function main() {
  const TelemetryVerifier = await ethers.getContractFactory("TelemetryVerifier");
  const telemetryVerifier = await TelemetryVerifier.deploy();
  await telemetryVerifier.waitForDeployment();
  console.log("TelemetryVerifier deployed to Sepolia at:", await telemetryVerifier.getAddress());

  const FundingVerifier = await ethers.getContractFactory("FundingVerifier");
  const fundingVerifier = await FundingVerifier.deploy();
  await fundingVerifier.waitForDeployment();
  console.log("FundingVerifier deployed to Sepolia at:", await fundingVerifier.getAddress());
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
