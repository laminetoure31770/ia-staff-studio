import {NextResponse} from 'next/server';
export function GET(){return NextResponse.json({status:'ok',service:'ia-staff-starter',version:'0.1.0'},{headers:{'Cache-Control':'no-store'}})}
