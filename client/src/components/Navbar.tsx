'use client'

import {
   Box,
   Flex,
   Avatar,
   Text,
   Button,
   Menu,
   MenuButton,
   MenuList,
   Image,
   MenuItem,
   MenuDivider,
   useColorModeValue,
   Stack,
   useColorMode,
   Center,
} from '@chakra-ui/react'
import { MoonIcon, SunIcon } from '@chakra-ui/icons'
import sumplus from '../assets/sumplus.png'
import doomguy from '../assets/doomguy.png'
import { Link } from 'react-router-dom'
export default function Navbar() {
   const { colorMode, toggleColorMode } = useColorMode()
   const lightmode = useColorModeValue('#1861C9', 'alternativeHexColorForLightMode')
   const darkmode = useColorModeValue('#171C26', 'alternativeHexColorForDarkMode')

   return (
      <div>
         <Box
            top="0"
            position="fixed"
            bg={useColorModeValue(lightmode, darkmode)}
            px={4}
            width="100%"
            zIndex={1000}
         >
            <Flex h={16} alignItems={'center'} justifyContent={'space-between'}>
               <Flex alignItems="center">
                  <Box>
                     <Image src={sumplus} height={50} />
                  </Box>
                  <Text ml={4} fontSize={'xl'} as={'b'}>
                     Sum Plus
                  </Text>
               </Flex>

               <Flex alignItems={'center'}>
                  <Stack direction={'row'} spacing={7}>
                     <Button onClick={toggleColorMode}>
                        {colorMode === 'light' ? <MoonIcon /> : <SunIcon />}
                     </Button>

                     <Menu>
                        <MenuButton
                           as={Button}
                           rounded={'full'}
                           variant={'link'}
                           cursor={'pointer'}
                           minW={0}
                        >
                           <Avatar size={'sm'} src={doomguy} />
                        </MenuButton>
                        <MenuList alignItems={'center'}>
                           <br />
                           <Center>
                              <Avatar size={'2xl'} src={doomguy} />
                           </Center>
                           <br />
                           <Center>
                              <p>Username</p>
                           </Center>
                           <br />
                           <MenuDivider />
                           <Link to={'/users'}>
                              <MenuItem>Users</MenuItem>
                           </Link>
                           <Link to={'/account'}>
                              <MenuItem>Account Settings</MenuItem>
                           </Link>
                           <Link to={'/journalentry'}>
                              <MenuItem>Journal Entry</MenuItem>
                           </Link>
                        </MenuList>
                     </Menu>
                  </Stack>
               </Flex>
            </Flex>
         </Box>
      </div>
   )
}
