const puppeteer = require('puppeteer');

const gpuUrl = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442"

async function initBrowser() {
    const browser = await puppeteer.launch({headless: false});
    const page = await browser.newPage();
    await page.goto(gpuUrl);
    return page;
}

async function checkStock() {
    
}

async function addToCart() {
    await page.$eval("button[class='add-to-cart-button']", elem => elem.click())

}