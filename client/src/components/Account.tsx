import Navbar from './Navbar.tsx'
import { Center, Box, Text } from '@chakra-ui/react'

export default function Account() {
   return (
      <div>
         <Navbar />
         <Box mt="4rem">
            <Center>
               <Text>Account Page</Text>
            </Center>
         </Box>
      </div>
   )
}
