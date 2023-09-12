import Navbar from './Navbar.tsx'
import { Center, Box, Text } from '@chakra-ui/react'

export default function Users() {
   return (
      <div>
         <Navbar />
         <Box mt="4rem">
            <Center>
               <Text>User List Page</Text>
            </Center>
         </Box>
      </div>
   )
}
