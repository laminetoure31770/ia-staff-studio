#!/usr/bin/env node
import {cpSync,existsSync,readdirSync,readFileSync,writeFileSync} from 'node:fs';
import {dirname,join,resolve,sep} from 'node:path';
import {fileURLToPath} from 'node:url';
const root=resolve(dirname(fileURLToPath(import.meta.url)),'../../../..');
const presets=join(root,'templates','distributions');
const starter=join(root,'templates','web-nextjs');
const models=readdirSync(presets).filter(n=>n.endsWith('.json')).map(n=>n.slice(0,-5));
const [action,model,dest]=process.argv.slice(2);
if(action==='list'){models.forEach(m=>console.log(m))}
else if(action==='init'){
 if(!model||!models.includes(model)||!dest)throw Error('Usage: ia-staff init <model> <directory>');
 const target=resolve(dest);
 if(existsSync(target))throw Error('Destination already exists');
 if(target===root||target.startsWith(root+sep))throw Error('Create the project outside the source repository');
 const manifest=JSON.parse(readFileSync(join(presets,model+'.json'),'utf8'));
 if(manifest.humanApproval!==true||manifest.deployAutomatically!==false)throw Error('Unsafe manifest');
 cpSync(starter,target,{recursive:true,errorOnExist:true,force:false});
 writeFileSync(join(target,'distribution.json'),JSON.stringify(manifest,null,2)+'\n');
 console.log('Created: '+target);
}else{console.error('Usage: ia-staff list | ia-staff init <model> <directory>');process.exitCode=1}
