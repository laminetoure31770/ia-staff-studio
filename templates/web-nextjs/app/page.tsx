import {readFile} from 'node:fs/promises';
import {join} from 'node:path';
type Distribution={name:string;description:string;status:string;modules:string[];humanApproval:boolean};
export const dynamic='force-dynamic';
async function load():Promise<Distribution|null>{
 try{return JSON.parse(await readFile(join(process.cwd(),'distribution.json'),'utf8')) as Distribution}catch{return null}
}
export default async function Home(){
 const model=await load();
 return <main style={{maxWidth:900,margin:'auto',padding:'60px 24px'}}>
 <p style={{color:'#b9e6c5'}}>IA STAFF · OPEN SOURCE</p>
 <h1>{model?.name??'IA STAFF Studio'}</h1>
 <p>{model?.description??'Generate a project using the Python or TypeScript CLI to select a profile.'}</p>
 <h2>Declared modules</h2>
 <ul>{(model?.modules??['Next.js starter']).map(x=><li key={x}>{x}</li>)}</ul>
 <p>Human review: {model?.humanApproval?'required':'not configured'}. Status: {model?.status??'generic starter'}.</p>
 <p><strong>Notice:</strong> These are configuration labels, not running agents, databases, authentication, or workflow engines.</p>
 </main>
}
